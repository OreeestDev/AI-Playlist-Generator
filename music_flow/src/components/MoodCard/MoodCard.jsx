import moods from '../../data/moods'
import './MoodCardStyles.css'

export default function MoodCard({ image, title, description }) {

//    const imagePath = new URL(`/src/assets/${image}`, import.meta.url).href;

    return (
        <div className='mood-card'>

            <div className='image-container'>
                <img src={`/assets/${image}`} alt=" " />
            </div>


            <h2>{title}</h2>
            <p>{description}</p>
        </div>
    );
}

