import React, { useState } from 'react';
import { httpService } from '../../http/httpService';
import { useNavigate } from 'react-router-dom';
import { Button, Card, Checkbox, Form, Input } from 'antd';


const loginPageStyle: React.CSSProperties = {
  textAlign: 'center',
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
}

type FieldType = {
  username?: string;
  password?: string;
};

const LoginPage = () => {
  let navigate = useNavigate();
  const onFinish = (values: any) => {
    httpService.login(values.username, values.password).then((data) => {
      const token = data.access_token;
      localStorage.setItem('token', token);
      httpService.setToken(token); // 设置全局 token
      // 导航到主页或其他页面
      navigate('/');
    }).catch((err) => {
      console.log(err);
    });
  };

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };
  return (
    <Form
      name="basic"
      labelCol={{ span: 8 }}
      wrapperCol={{ span: 16 }}
      style={loginPageStyle}
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      <h3>登录</h3>
      <Form.Item<FieldType>
        label="登录邮箱"
        name="username"
        rules={[{ required: true, message: 'Please input your email!' }]}
      >
        <Input type='email' />
      </Form.Item>

      <Form.Item<FieldType>
        label="Password"
        name="password"
        rules={[{ required: true, message: 'Please input your password!' }]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
        <Button type="primary" htmlType="submit">
          登录
        </Button>
      </Form.Item>
    </Form>
  );
};

export default LoginPage;
