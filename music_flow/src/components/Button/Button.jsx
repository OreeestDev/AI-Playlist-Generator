import './Button.css'

export default function Button({children}) {

    function handleClick() {
        console.log('send mood to AI')
    }

    return <button className='button' onClick={handleClick}>{children}</button>
}