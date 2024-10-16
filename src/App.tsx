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
                const temp = await window.pyloid.custom.bindDeviceID(key);
                if (temp==1) {
                  success("激活成功");
                } else if (temp==0) {
                  error("激活失败");
                }
                else if (temp==-1){
                  error("密钥已使用, 不进行任何操作")
                }
                else {
                  error("密钥无效");
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
