import { Button, Input, message, Spin } from "antd";
import { Column, FullScreen, Sizedbox, vspace20 } from "leo-react";
import FSFLogo from "/fst.jpg";
import { useState, useEffect } from "react";
import AutokeyApp from "./pages/Autokey.tsx";

function App() {
  const [messageApi, contextHolder] = message.useMessage();
  const [key, setKey] = useState("");
  const [valid, setValid] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const loadKey = async () => {
      try {
        const storedKey = await window.pyloid.custom.load_key();
        setKey(storedKey);
      } catch (err) {
        console.error("Error loading key:", err);
      }
    };

    loadKey();
  }, []);

  const success = () => {
    messageApi.open({
      type: "success",
      content: "登录成功",
    });
  };
  const error = () => {
    messageApi.open({
      type: "error",
      content: "无效",
    });
  };

  const handleLogin = async () => {
    setLoading(true);
    try {
      await new Promise((resolve) => setTimeout(resolve, 500)); // 延迟 500 毫秒
      const temp = await window.pyloid.custom.verify_key(key);
      if (temp === 1) {
        success();
        await window.pyloid.custom.store_key(key);
        setValid(true);
      } else {
        error();
      }
    } catch (err) {
      error();
    }
    setLoading(false);
  };

  if (valid) {
    return <AutokeyApp />;
  }

  return (
    <FullScreen>
      {contextHolder}
      <Column mainAxisAlignment="flex-start" crossAxisAlignment="center">
        {vspace20}
        {vspace20}
        <img src={FSFLogo} width="50%"></img>
        <h2>自由足球按键精灵</h2>
        <Sizedbox width="40%">
          <Input
            placeholder="输入你的密钥"
            value={key}
            onChange={(e) => setKey(e.target.value)}
          ></Input>
        </Sizedbox>
        {vspace20}
        <Button onClick={handleLogin} disabled={loading}>
          {loading ? <Spin size="small" /> : "登录"}
        </Button>
      </Column>
    </FullScreen>
  );
}

export default App;