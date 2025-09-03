import { useState } from 'react';

function App() {
  const courses = ["Programowanie w C#", "Angular dla początkujących", "Kurs Django"]

  const [currCourse, setCurrCourse] = useState(0)
  const [name, setName] = useState("")

  function handleSubmit() {
    console.log(`name: ${name}`)
    let course = courses[parseInt(currCourse) - 1]
    
    if(course === undefined) {
      console.log("Nie ma takiego kursu")
    }
    else {
      console.log(course)
    }
  }

  return (
    <>
    <h1> 
      Liczba kursów: {courses.length}
    </h1>
    <ul>
      {courses.map((course, id) => {
        return <li id={`course-${id}`} key={id}>{course}</li>
      })}
    </ul>
    <form onSubmit={(e) => { e.preventDefault(); handleSubmit(); }}>
      <label id='name'>
        Imię i nazwisko
      </label>
      <br></br>
      <input type='text' name='name' onChange={(e)=>{setName(e.target.value)}}></input>
      <br></br>
      <br></br>
      <label id='course_number'>
        Numer kursu
      </label>
      <br></br>
      <input type='number' name='course_number' value={currCourse} onChange={(e)=>{setCurrCourse(e.target.value)}}></input>
      <br></br>
      <br></br>
      <button>
        Zapisz do kursu
      </button>
    </form>
    </>
  );
}

export default App;
