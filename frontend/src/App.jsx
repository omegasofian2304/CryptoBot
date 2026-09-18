import { Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Tendance from './pages/Tendance'
import Graphiques from './pages/Graphiques'
import Options from './pages/Options'
import Strategies from './pages/Strategies'

function App() {
    return (
        <>
            <Header />
            <Routes>
                <Route path="/" element={<Tendance />} />
                <Route path="/graphiques" element={<Graphiques />} />
                <Route path="/Options" element={<Options />} />
                <Route path="/Stratégies" element={<Strategies />} />
            </Routes>
        </>
    )
}

export default App