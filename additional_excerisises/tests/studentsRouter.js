const express = require('express');
const router = express.Router();

// Assume we have a database connection
const db = require('./database');

/**
 * GET /students - Retrieves all students from database
 * 
 * FLAWS: Missing pagination causes performance degradation with large datasets (10k+ records).
 * No query parameter validation allows SQL injection via sort/filter params. Error logging uses
 * console.log instead of proper logger, losing timestamp/severity context. Doesn't handle database
 * connection failures gracefully - crashes instead of returning 503. Missing rate limiting enables
 * DOS attacks. Response doesn't include metadata like total count or has_more flag for pagination.
 * 
 * TODO: Implement limit/offset pagination with max 100 records per request
 * TODO: Add Winston logger with structured logging and log levels
 * TODO: Implement express-rate-limit middleware (100 requests/15min)
 * TODO: Add input validation with Joi for query parameters
 */
router.get('/students', async (req, res) => {
  try {
    const students = await db.query('SELECT * FROM students');
    console.log('Retrieved students');
    res.json(students);
  } catch (error) {
    console.log('Error:', error);
    res.status(500).json({ error: 'Failed to retrieve students' });
  }
});

/**
 * GET /students/:id - Retrieves single student by ID
 * 
 * FLAWS: Doesn't validate ID format before query - accepts strings like "abc" causing database errors.
 * Vulnerable to timing attacks since 404 response differs from 500 timing. Logging exposes full student
 * record including sensitive PII to console. No authorization check allows any authenticated user to
 * view any student. Doesn't handle soft-deleted records (deleted_at field) so returns deleted students.
 * Missing cache headers causes repeated database hits.
 * 
 * TODO: Add express-validator to check ID is numeric and positive integer
 * TODO: Implement role-based access control (RBAC) middleware to verify student ownership
 * TODO: Redact sensitive fields (SSN, DOB) from logs or use sanitized logging
 * TODO: Add WHERE deleted_at IS NULL to query filter
 */
router.get('/students/:id', async (req, res) => {
  try {
    const student = await db.query('SELECT * FROM students WHERE id = ?', [req.params.id]);
    console.log('Found student:', student);
    
    if (!student) {
      return res.status(404).json({ error: 'Student not found' });
    }
    
    res.json(student);
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: 'Database error' });
  }
});

/**
 * POST /students/search - Search students by criteria
 * 
 * FLAWS: Accepts any JSON payload without schema validation enabling malicious queries. Dynamically
 * builds WHERE clause from request body creating SQL injection vulnerability. No input sanitization
 * on search terms allows special characters to break queries. Logging only captures "search performed"
 * without criteria details making debugging impossible. Doesn't limit result set enabling data exfiltration.
 * Missing index on searchable fields causes full table scans. Case-sensitive search excludes valid matches.
 * 
 * TODO: Replace string concatenation with parameterized queries using placeholders
 * TODO: Add request body validation schema with ajv or express-validator
 * TODO: Implement LIMIT 50 on query and add result count to logs
 * TODO: Use ILIKE or LOWER() for case-insensitive matching
 */
router.post('/students/search', async (req, res) => {
  try {
    const { name, email, grade } = req.body;
    
    let query = 'SELECT * FROM students WHERE 1=1';
    if (name) query += ` AND name LIKE '%${name}%'`;
    if (email) query += ` AND email = '${email}'`;
    if (grade) query += ` AND grade = ${grade}`;
    
    const results = await db.query(query);
    console.log('Search performed');
    res.json(results);
  } catch (error) {
    console.log('err');
    res.status(500).json({ error: 'Search failed' });
  }
});

module.exports = router;