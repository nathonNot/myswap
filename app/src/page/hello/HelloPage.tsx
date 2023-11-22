import { useEffect, useState } from 'react';
import { Card, CardBody } from "@nextui-org/react";
import { httpService } from '../../http/httpService';


export default function HelloPage() {
    const [allMoney, setAllMoney] = useState(0);

    useEffect(() => {
        // 获取总金额
        httpService.getAllMoney().then(money => {
            setAllMoney(money);
        });
    }, []);

    return (
        <Card>
            <CardBody>
                <p>当前总金额{allMoney}$</p>
            </CardBody>
        </Card>
    );
}