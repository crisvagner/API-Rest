import './styles.css';

export default function Home() {
  const pagina = 'red'; // 'red'

  if (pagina === 'blue') {
    return (
      <div className="App">
        <header className="App-header">
          <p>
            SÓ BORA!!!
          </p>
        </header>
      </div>
    );

  } else if (pagina === 'red') {
    return (
      <div className="App">
        <header className="App-header-2 App-header">
          <p>
            AO INFINITO E ALÉM!!!
          </p>
        </header>
      </div>
    );
  } else {
    return (
      <div className="App">
        <header className="App-header-3 App-header">
          <p>
            ESTA ROTA NÃO EXISTE!!!
          </p>
        </header>
      </div>
    );
  }
}
