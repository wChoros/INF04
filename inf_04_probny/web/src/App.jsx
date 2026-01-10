import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import ProductCard from './ProductCard';
import { products } from './products'
import { useState } from 'react';


function App() {
  const [categoriesVisible, setCategoriesVisible] = useState({
    "Meble": true,
    "Elektronika": true,
    "Akcesoria": true
  })

  return (
    <div className="container py-5">
      <div className="row">
        <div className="col-12 my-3 p-0">
          <h1>Galeria produktów</h1>
        </div>
        <div className="col-12 d-flex gap-5 p-0 my-3 form-check form-switch">
          <label className="form-check-label" htmlFor="electronics">Elektronka</label>
          <input className="form-check-input" type="checkbox" id="electronics" name="electronics" checked={categoriesVisible["Elektronika"]} onChange={(e) => setCategoriesVisible({...categoriesVisible, "Elektronika": e.target.checked})}></input>
          <label className="form-check-label" htmlFor="furniture" >Meble</label>
          <input className="form-check-input" type="checkbox" id="furniture" name="furniture" checked={categoriesVisible["Meble"]} onChange={(e) => setCategoriesVisible({...categoriesVisible, "Meble": e.target.checked})}></input>
          <label className="form-check-label" htmlFor="accessories">Akcesoria</label>
          <input className="form-check-input" type="checkbox" id="accessories" name="accessories"checked={categoriesVisible["Akcesoria"]} onChange={(e) => setCategoriesVisible({...categoriesVisible, "Akcesoria": e.target.checked})}></input>
        </div>
      </div>
      <div className="row">
        {products.map((product) =>
          <ProductCard product={product} key={product.id} categoriesVisible={categoriesVisible}/>
        )}
      </div>
    </div>
  );
}

export default App;
