import Countdown from '../components/Countdown';

export default function Home() {
  const targetDate = '2024-12-31T00:00:00';

  return (
    <div style={{ textAlign: 'center', padding: '50px' }}>
      <h1>Countdown to New Year</h1>
      <Countdown targetDate={targetDate} />
    </div>
  );
}
