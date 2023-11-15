// ProtectedRoute.tsx
import React, { ReactNode } from 'react';
import { Navigate } from 'react-router-dom';

interface ProtectedRouteProps {
  children: ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const token = localStorage.getItem('token');

  if (!token) {
    // 用户未登录，重定向到登录页面
    return <Navigate to="/login" />;
  }

  return <>{children}</>;
};

export default ProtectedRoute;
