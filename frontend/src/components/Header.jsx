import logo from '../logo.svg'

export default function Header() {

    const time = new Date()
    const alt = 'Alternative'

    return (
      <header>
      {/* <img src={logo} alt={alt} />  */}
      <span>Music time: {time.toLocaleTimeString()}</span>
    </header>
    )
}