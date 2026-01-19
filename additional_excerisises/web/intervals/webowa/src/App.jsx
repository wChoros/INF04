import './App.css';
import 'bootstrap/dist/css/bootstrap.css'
import {useEffect, useState} from "react";


function App() {
    const videos = [
        "deszcz.mp4",
        "morze.mp4",
        "plaza.mp4",
        "ptak.mp4",
        "samochod.mp4"
    ]

    const [currVideo, setCurrVideo] = useState(0)

    useEffect(() => {
        console.log(videos[currVideo])
        const timeoutId = setTimeout(() => {
            setCurrVideo(prevState => (prevState + 1) % videos.length)
        }, 5000)

        return () => {
            clearTimeout(timeoutId)
        }
    }, [currVideo, videos])

    return (
        <div className="App row">
            <div className='col d-flex align-items-center justify-content-center'>
                <input type='button' className='btn btn-primary' value='<' onClick={() => {
                    setCurrVideo(prevState => prevState === 0 ? videos.length - 1 : (prevState - 1) % videos.length)
                }}/>
            </div>
            <div className='col'>
                <h1>
                    Video Player
                </h1>
                <p>Current Video: {videos[currVideo]}</p>
                <video autoPlay src={"assets/" + videos[currVideo]}/>
            </div>
            <div className='col d-flex align-items-center justify-content-center'>
                <input type='button' className='btn btn-primary' value='>' onClick={()=>{
                    setCurrVideo(prevState => (prevState + 1) % videos.length)
                }}/>
            </div>
        </div>
    );
}

export default App;
