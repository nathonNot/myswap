import LoginPage from './page/login/LoginPage';
import HelloPage from './page/hello/HelloPage';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ProtectedRoute from './route/ProtectedRoute';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <HelloPage />
            </ProtectedRoute>
          }
        />
        {/* 更多路由 */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;
