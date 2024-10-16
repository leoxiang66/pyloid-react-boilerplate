import { Button } from "antd";
import { Column, FullScreen, vspace20 } from "leo-react";

function AutokeyApp() {
  return (
    <FullScreen>
      <Column mainAxisAlignment="flex-start" crossAxisAlignment="center">
        {vspace20}
        {vspace20}
        {vspace20}
        <Button onClick={()=>window.pyloid.custom.print_info()}>启动</Button>
      </Column>
    </FullScreen>
  );
}

export default AutokeyApp;
