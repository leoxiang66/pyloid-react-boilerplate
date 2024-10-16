import { Button, Input, message } from "antd";
import { Column, FullScreen, Sizedbox, vspace20 } from "leo-react";
import FSFLogo from "/fst.jpg";
import { useState } from "react";
import AutokeyApp from "./pages/Autokey.tsx";

function App() {
  const [messageApi, contextHolder] = message.useMessage();
  const [key, setKey] = useState("");
  const [valid, setValid] = useState(false);

  const success = () => {
    messageApi.open({
      type: 'success',
      content: '登录成功',
    });
  };
  const error = () => {
    messageApi.open({
      type: 'error',
      content: '密码错误',
    });
  };

  if (valid) {
    return (<AutokeyApp />)
  }

  return (
    <FullScreen>
      {contextHolder}
      <Column mainAxisAlignment="flex-start" crossAxisAlignment="center">
        {vspace20}
        {vspace20}
        <img src={FSFLogo} width="40%"></img>
        {vspace20}
        <h2>自由足球按键精灵</h2>
        <Sizedbox width="40%">
          <Input placeholder="输入你的密钥" onChange={(e)=>setKey(e.target.value)}></Input>
        </Sizedbox>
        {vspace20}
        <Button onClick={() => {
          if (key == "123") {
            success();
            setValid(true);
          } else {
            error();
          }
        }}>
          登录
        </Button>
      </Column>
    </FullScreen>
  );
}

export default App;
