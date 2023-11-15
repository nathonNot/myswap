import React, { useState } from 'react';
import { Input, Button, Card } from '@nextui-org/react';
import axios from 'axios';

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      axios.post('https://your-api-url.com/login', { username, password })
        .then(response => {
          const token = response.data.token;
          localStorage.setItem('token', token);
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          // 导航到主页或其他页面
        })
        .catch(error => {
          // 处理登录错误
        });

      // 保存 token 到本地存储或状态管理库
      // localStorage.setItem('token', token);

    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.error('Login error', error.response);
      } else {
        console.error('Unexpected error', error);
      }
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
