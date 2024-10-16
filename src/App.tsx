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
  const success = (msg:string) => {
    messageApi.open({
      type: "success",
      content: msg,
    });
  };
  const error = (msg:string) => {
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
        <h1>单点登录密钥生成器</h1>
        {vspace20}
        <Sizedbox width="50%">
          <Row>
            <Input value={key} />
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
              生成
            </Button>
            {hspace20}
            <Button
              onClick={async () => {
                const res = await window.pyloid.custom.copy2clipoard(key);
                if (res) {
                  success("复制成功");
                } else {
                  error("复制失败");
                }
              }}
            >
              复制
            </Button>
          </Row>
        </Sizedbox>
        {vspace20}
        {vspace20}
      </Column>
    </FullScreen>
  );
}

export default App;
