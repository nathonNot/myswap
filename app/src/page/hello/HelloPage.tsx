import { useEffect, useState } from 'react';
import { httpService } from '../../http/httpService';
import { Col, Flex, Layout, List, Radio, Row, Space, } from 'antd';
import { Content, Header } from 'antd/es/layout/layout';

const headerStyle: React.CSSProperties = {
    textAlign: 'center',
    color: '#fff',
    height: 64,
    paddingInline: 50,
    lineHeight: '64px',
    backgroundColor: '#7dbcea',
};

const contentStyle: React.CSSProperties = {
    textAlign: 'center',
    minHeight: 120,
    lineHeight: '120px',
    color: '#fff',
    backgroundColor: '#108ee9',
};

const data = [
    'Racing car sprays burning fuel into crowd.',
    'Japanese princess to wed commoner.',
    'Australian walks 100km after outback crash.',
    'Man charged over missing wedding girl.',
    'Los Angeles battles huge wildfires.',
];

export default function HelloPage() {
    const [allMoney, setAllMoney] = useState(0);
    useEffect(() => {
        // 获取总金额
        httpService.getAllMoney().then(money => {
            if (money >= 0) {
                setAllMoney(money);
            }
        });
    }, []);

    return (
        <Layout>
            <Header style={headerStyle}>Header</Header>
            <Content style={contentStyle}>
                <Row>
                    <Col span={24}>
                        <Flex gap="middle" vertical>
                            <Flex vertical={false}>
                                <div>总金额:{allMoney}$</div>
                                {Array.from({ length: 4 }).map((_, i) => (
                                    <div key={i} style={{ backgroundColor: i % 2 ? '#1677ff' : '#1677ffbf' }} ></div>
                                ))}
                            </Flex>
                        </Flex>

                    </Col>
                </Row>

                <Row>
                    <List
                        size="small"
                        bordered
                        dataSource={data}
                        renderItem={(item) => <List.Item>{item}</List.Item>}
                    />
                </Row>
            </Content>
        </Layout>
    );
}