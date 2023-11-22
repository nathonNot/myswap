// ProtectedRoute.tsx
import React, { ReactNode } from 'react';
import { Navigate, useNavigate } from 'react-router-dom';
import { httpService } from '../http/httpService';

interface ProtectedRouteProps {
  children: ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const token = localStorage.getItem('token');
  
  if (token == "" || token == "undefined" || token == null || token == "null") {
    // 用户未登录，重定向到登录页面
    console.log('用户未登录，重定向到登录页面');
    
    return <Navigate to="/login" />;
  }
  httpService.checkToken(token).then((success) => {
    if (!success) {
      localStorage.removeItem('token');
      return <Navigate to="/login" />;
    }
  });

  return <>{children}</>;
};

export default ProtectedRoute;
