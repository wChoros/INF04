import './index.css';
import 'bootstrap/dist/css/bootstrap.css';
import { students as studentsComp } from '../../data/students.js';
import { use, useState } from 'react';
function App() {
  const [students, setStudents] = useState(studentsComp)
  const [name, setName] = useState("")
  const [grade, setGrade] = useState("")
  const [showBadStudents, setShowBadStudents] = useState(true)
  return (
    <>
      <h1>Lista uczniów</h1>
      <form action="" className=''>
        <label htmlFor="name" >Imię i nazwisko ucznia</label> <br />
        <input type="text" id='name' value={name} onChange={(e) => {
          setName(e.target.value)
        }} /> <br />

        <label htmlFor="grade" >Ocena</label> <br />
        <select name="grade" id="grade" className='form-select' value={grade} onChange={(e) => { setGrade(e.target.value) }}>
          <option value=""></option>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
        </select> <br />
        <input type='button' className='btn btn-primary' value='Dodaj Ucznia' onClick={(e) => {
          e.preventDefault()
          if (!grade || !name) {
            alert("Pola muszą być wypełnione")
          }
          else {
            setStudents([
              ...students,
              {
                id: students.length + 1,
                name: name,
                grade: grade
              }
            ])
          }
        }} /> <br />

        <div className='form-check form-switch'>
          <label htmlFor="studentsWithHighGrade" className='form-check-label'>Pokaż tylko uczniów z oceną powyżej 3</label>
          <input className="form-check-input" type="checkbox" name="studentsWithHighGrade" id="studentsWithHighGrade" onChange={(e) => {
            setShowBadStudents(!e.target.checked)
          }} /> <br />
        </div>
      </form>
      <div className='table-responsive'>
        <table className='table table-bordered table-striped'>
          <thead>
            <tr>
              <th>Imię i nazwisko</th>
              <th>Ocena</th>
            </tr>
          </thead>
          <tbody>
            {students.map((student, i) => {
              if (!showBadStudents && student.grade < 3)
                return <></>
              else
                return <tr key={student.id}>
                  <td>{student.name}</td>
                  <td>{student.grade}</td>
                </tr>
            })}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default App;
