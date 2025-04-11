import './MoodCardStyles.css'
import MoodCard from './MoodCard'

export default function MoodGrid( { moods }) {
    return (

        <div className='mood-grid'>
            {moods.map((mood, index) => (
            <MoodCard 
            key={index}
            image={mood.image}
            title={mood.title}
            description={mood.description}
            />
            ))}
        </div>

    )
}