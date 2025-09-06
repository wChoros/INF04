import './App.css';
import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  const pictures = [
    { id: 0, alt: "Mak", filename: "obraz1.jpg", category: 1, downloads: useState(35) },
    { id: 1, alt: "Bukiet", filename: "obraz2.jpg", category: 1, downloads: useState(43) },
    { id: 2, alt: "Dalmatyńczyk", filename: "obraz3.jpg", category: 2, downloads: useState(2) },
    { id: 3, alt: "Świnka morska", filename: "obraz4.jpg", category: 2, downloads: useState(53) },
    { id: 4, alt: "Rotwailer", filename: "obraz5.jpg", category: 2, downloads: useState(43) },
    { id: 5, alt: "Audi", filename: "obraz6.jpg", category: 3, downloads: useState(11) },
    { id: 6, alt: "kotki", filename: "obraz7.jpg", category: 2, downloads: useState(22) },
    { id: 7, alt: "Róża", filename: "obraz8.jpg", category: 1, downloads: useState(33) },
    { id: 8, alt: "Świnka morska", filename: "obraz9.jpg", category: 2, downloads: useState(123) },
    { id: 9, alt: "Foksterier", filename: "obraz10.jpg", category: 2, downloads: useState(22) },
    { id: 10, alt: "Szczeniak", filename: "obraz11.jpg", category: 2, downloads: useState(12) },
    { id: 11, alt: "Garbus", filename: "obraz12.jpg", category: 3, downloads: useState(321) }
  ]

  const [flowersView, setFlowersView] = useState(true)
  const [animalsView, setAnimalsView] = useState(true)
  const [carsView, setCarsView] = useState(true)

  return (
    <>
      <h1>
        Kategorie zdjęć
      </h1>
      <div className="form-check form-switch form-check-inline">
      <label htmlFor="flowers" className='form-check-label'>Kwiaty</label>
      <input type="checkbox" name="flowers" id="flowers" className='form-check-input' checked={flowersView} onClick={() => {
        setFlowersView(flowersView ? false : true)
      }} />
      </div>

      <div className="form-check form-switch form-check-inline">
        <label htmlFor="animals" className='form-check-label'>Zwierzęta</label>
        <input type="checkbox" name="animals" id="animals" className='form-check-input' checked={animalsView} onClick={() => {
          setAnimalsView(animalsView ? false : true)
        }} />
      </div>
      <div className="form-check form-switch form-check-inline">
        <label htmlFor="cars" className='form-check-label'>Samochody</label>
        <input type="checkbox" name="cars" id="cars" className='form-check-input' checked={carsView} onClick={() => {
          setCarsView(carsView ? false : true)
        }} />
      </div>

      <div className='picture-canvas'>
      {pictures.map((picture) => {
        switch (picture.category) {
          case (1):
            return <div hidden={!flowersView} className='picture-container'>
              <img src={`assets/${picture.filename}`} alt={picture.alt}/>
              <h4>Pobrań: {picture.downloads[0]}</h4>
              <button className='btn btn-success' onClick={() => {
                picture.downloads[1](picture.downloads[0] + 1)
              }}>Pobierz</button>
            </div>
          case (2):
            return <div hidden={!animalsView} className='picture-container'>
              <img src={`assets/${picture.filename}`} alt={picture.alt} />
              <h4>Pobrań: {picture.downloads[0]}</h4>
              <button className='btn btn-success' onClick={() => {
                picture.downloads[1](picture.downloads[0] + 1)
              }}>Pobierz</button>
            </div>
          case (3):
            return <div hidden={!carsView} className='picture-container'>
              <img src={`assets/${picture.filename}`} alt={picture.alt} />
              <h4>Pobrań: {picture.downloads[0]}</h4>
              <button className='btn btn-success' onClick={() => {
                picture.downloads[1](picture.downloads[0] + 1)
              }}>Pobierz</button>
            </div>
          default:
            return null;
        }
      })}
    </div>

    </>
  );
}

export default App;
