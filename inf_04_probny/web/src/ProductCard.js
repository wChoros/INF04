import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';

function ProductCard(props) {
  const product = props.product

  const [likes, setLikes] = useState(product.likes)
  

  return (
    <div className="col-12 col-md-4 py-2" hidden={!props.categoriesVisible[product.category]}>
      <div className="card">
        <img src={"assets/"+product.filename} className="card-img-top" alt="..."/>
          <div className="card-body">
            <h5 className="card-title">{product.name}</h5>
            <p className="card-text">
              {product.description}
            </p>
            <button className="btn btn-primary" onClick={()=>{setLikes(likes+1)}}>Liczba polubień: {likes}</button>
          </div>
      </div>
    </div>
  );
}

export default ProductCard;
