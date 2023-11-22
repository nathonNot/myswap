import React, { useState } from 'react';
import { Input, Button, Card } from '@nextui-org/react';
import { httpService } from '../../http/httpService';
import { useNavigate } from 'react-router-dom';


const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  let navigate = useNavigate();

  const handleLogin = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const data = await httpService.login(username, password);
      const token = data.access_token;
      localStorage.setItem('token', token);
      httpService.setToken(token); // 设置全局 token
      // 导航到主页或其他页面
      navigate('/');
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <Card>
      <form style={{ padding: '20px' }} onSubmit={handleLogin}>
        <h3 style={{ textAlign: 'center' }}>登录</h3>
        <Input
          isClearable
          placeholder="用户名"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={{ marginTop: '10px' }}
        />
        <Input
          isClearable
          placeholder="密码"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ marginTop: '10px' }}
        />
        <Button type="submit" style={{ marginTop: '20px' }}>登录</Button>
      </form>
    </Card>
  );
};

export default LoginPage;
