import './App.css';
import Header from './components/Header'
import Button from './components/Button/Button';
import MoodCard from './components/MoodCard/MoodCard';
import moods from './data/moods.js'
import MoodGrid from './components/MoodCard/MoodGrid';

export default function App() {
  return (
      <div> 

{/* <Button> */}

        <MoodGrid moods={moods}/>


{/* </Button> */}

      </div>
  );
}
