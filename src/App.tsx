import { Button } from 'antd';
import { Column, FullScreen, hspace20, vspace20 } from 'leo-react';

function App() {
  return (
    <FullScreen>
      <Column mainAxisAlignment='flex-start' crossAxisAlignment='center'>
        {vspace20}
        {vspace20}
        <h1>你好</h1>
        {vspace20}
        <p>This is an antd button</p>
        <Button type='primary' onClick={()=> window.pyloid.custom.print_info()}>Antd Button</Button>


      </Column>
    </FullScreen>
  );
}

export default App;
