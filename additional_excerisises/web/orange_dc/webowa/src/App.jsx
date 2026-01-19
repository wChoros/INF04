import {useEffect, useState} from 'react';
import 'bootstrap/dist/css/bootstrap.css'
import './App.css';


function addView(videos, videoId) {
    return videos.map((video) => {
        if (video.id === videoId) {
            return {...video, wyswietlenia: video.wyswietlenia + 1}
        }
        return video
    })
}

function addLike(videos, videoId) {
    return videos.map((video) => {
        if (video.id === videoId) {
            return {...video, polubienia: video.polubienia + 1}
        }
        return video
    })
}

function App() {

    const [videos, setVideos] = useState([
        {id: 1, tytul: "Deszcz", plik: "deszcz.mp4", polubienia: 5, wyswietlenia: 11, autor: 'maciek544'},
        {id: 2, tytul: "Słoneczna plaża", plik: "plaza.mp4", polubienia: 3, wyswietlenia: 6, autor: 'jacek55'},
        {id: 3, tytul: "Fale morza", plik: "morze.mp4", polubienia: 5, wyswietlenia: 8, autor: '_.joasia._'},
        {id: 4, tytul: "Samochód", plik: "samochod.mp4", polubienia: 20, wyswietlenia: 45, autor: 'mareczek_51'},
        {id: 5, tytul: "Ptak i śnieg", plik: "ptak.mp4", polubienia: 8, wyswietlenia: 24, autor: 'marysia_284'},
    ])


    const [currVideoId, setCurrVideoId] = useState(1)

    useEffect(() => {
        setVideos(addView(videos, 1))
    }, [])

    return <div className='row '>
        <div className="col">
            <video src={"assets/" + videos[currVideoId - 1].plik} controls/>
            <h2>{videos[currVideoId - 1].tytul}</h2>
            <p>
                Dodany przez: {videos[currVideoId - 1].autor},
                polubień: {videos[currVideoId - 1].polubienia},
                wyświetleń: {videos[currVideoId - 1].wyswietlenia},
            </p>
            <p>
                <button className='btn btn-primary' onClick={() => {
                    setVideos(addLike(videos, currVideoId))
                }}>Lubię to!
                </button>
            </p>
        </div>
        <div className='col'>
            <h1>Zobacz też inne filmy</h1>
            <ul className='list-group'>
                {videos.map((video) => {
                    return <li key={video.id} className='list-group-item' onClick={() => {
                        console.log(video)
                        setCurrVideoId(video.id)
                        setVideos(addView(videos, video.id))
                    }}>
                        {video.tytul}
                    </li>
                })}
            </ul>
        </div>
    </div>
}

export default App;
