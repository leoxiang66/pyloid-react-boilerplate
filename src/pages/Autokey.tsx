import { FullScreen, Column, vspace20, Clickable } from "leo-react";
import { useState, useRef } from "react";

function AutokeyApp() {
  const [isStarted, setIsStarted] = useState(false);
  const [timer, setTimer] = useState(0);
  const timerRef = useRef(null);

  const handleClick = () => {
    if (!isStarted) {
      startTimer();
      window.pyloid.custom.start();
    } else {
      stopTimer();
      window.pyloid.custom.stop();
    }
    setIsStarted(!isStarted);
  };

  const startTimer = () => {
    const startTime = Date.now();
    timerRef.current = setInterval(() => {
      setTimer(Math.floor((Date.now() - startTime) / 1000));
    }, 1000);
  };

  const stopTimer = () => {
    clearInterval(timerRef.current);
    setTimer(0);
  };

  return (
    <FullScreen>
      <Column mainAxisAlignment="center" crossAxisAlignment="center">
        <Clickable onClick={handleClick}>
          <div
            style={{
              width: "100px",
              height: "100px",
              borderRadius: "50%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              backgroundColor: isStarted ? "#4caf50" : "grey",
              boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
              cursor: "pointer",
              transition: "box-shadow 0.3s ease-in-out, background-color 0.3s ease-in-out",
            }}
            className="hover:shadow-lg"
          >
            <img src="/start.png" alt="Start" style={{ width: "60px" }} />
          </div>
        </Clickable>
        {vspace20}
        <div className="text-8xl text-gray-700">{timer}s</div>
      </Column>
    </FullScreen>
  );
}

export default AutokeyApp;