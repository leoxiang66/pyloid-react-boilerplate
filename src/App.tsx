import { Button, Input, message } from "antd";
import {
  Column,
  FullScreen,
  hspace20,
  vspace20,
  Row,
  Sizedbox,
} from "leo-react";
import { useState } from "react";

function App() {
  const [key, setKey] = useState("");
  const [messageApi, contextHolder] = message.useMessage();
  const success = (msg: string) => {
    messageApi.open({
      type: "success",
      content: msg,
    });
  };
  const error = (msg: string) => {
    messageApi.open({
      type: "error",
      content: msg,
    });
  };

  return (
    <FullScreen>
      {contextHolder}
      <Column mainAxisAlignment="flex-start" crossAxisAlignment="center">
        {vspace20}
        {vspace20}
        <h1>激活器</h1>
        {vspace20}
        <Sizedbox width="50%">
          <Row>
            <Input
              placeholder="输入你的专属密钥"
              onChange={(e) => setKey(e.target.value)}
            />
            {hspace20}
            <Button
              onClick={async () => {
                try {
                  const temp =
                    await window.pyloid.custom.generate_random_string();
                  const tempStr = temp.toString();
                  setKey(tempStr);
                } catch (error) {
                  console.error("Error generating string:", error);
                }
              }}
            >
              激活
            </Button>
          </Row>
        </Sizedbox>
      </Column>
    </FullScreen>
  );
}

export default App;
