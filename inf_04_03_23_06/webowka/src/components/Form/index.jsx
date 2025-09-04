import { useState } from 'react';
import './style.css';
import 'bootstrap/dist/css/bootstrap.css'


function Form() {
  const [title, setTitle] = useState("")
  const [genre, setGenre] = useState("")

  function handleSubmit() {
    console.log(`tytul: ${title}; rodzaj: ${genre}`)
  }

  return (
    <form onSubmit={(e)=>{e.preventDefault()}} className='form-group'>
      <label htmlFor="title">
        Tytuł filmu
      </label>
      <input type="text" id='title' onChange={(e)=>{setTitle(e.target.value)}} value={title} className='form-control'/>
      <label htmlFor="genre">
        Rodzaj
      </label>
      <select name="genre" id="genre" onChange={(e)=>{setGenre(e.target.value)}} value={genre} className='form-control'>
        <option value=""></option>
        <option value="1">Komedia</option>
        <option value="2">Obyczajowy</option>
        <option value="3">Sensacyjny</option>
        <option value="4">Horror</option>
      </select>
      <button type='button' className='btn btn-success' onClick={()=>{handleSubmit()}}>
        Zapisz
      </button>
    </form>
  );
}

export default Form;
