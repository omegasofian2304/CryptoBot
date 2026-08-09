import { NavLink } from 'react-router-dom'

export default function Header() {


    const active = "inline-block text-white bg-[rgb(26,26,29)] rounded-xl px-4 py-2"
    const inactive = "inline-block rounded-xl px-4 py-2 text-[rgba(138,138,143,1)]"
    return (
        <header className="flex w-full items-center h-20 bg-[rgba(10,10,11,1)] text-xl text-white select-none">
            <div className="h-full flex w-1/5 items-center"><p className="text-white ml-20">Crypto</p><p className="text-amber-300">Bot</p></div>
            <nav className="flex-1 h-full" >
                <ul className="flex items-center justify-center gap-10 h-full">
                    <li>
                        <NavLink to="/" className={({ isActive }) => isActive ? active : inactive}>
                            Tendance
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/graphiques" className={({ isActive }) => isActive ? active : inactive}>
                            Graphiques
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/options" className={({ isActive }) => isActive ? active : inactive}>
                            Options
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/stratégies" className={({ isActive }) => isActive ? active : inactive}>
                            Stratégies
                        </NavLink>
                    </li>

                </ul>
            </nav>
            <div className="h-full flex w-1/5 justify-center items-center text-[rgba(138,138,143,1)]">
                <div className="flex items-center gap-2 bg-[rgb(16,16,19)] px-4 py-2 rounded-full border-2 border-[rgba(30,30,34,1)] ">
                    <span className="w-2 h-2 rounded-full bg-green-500"></span>
                    <p>API connectée</p>
                </div>
            </div>        </header>
    );
}