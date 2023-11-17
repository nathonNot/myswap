import { useState } from 'react';
import { Card, CardBody } from "@nextui-org/react";


export default function HelloPage() {
    const [allMoney] = useState(0);

    return (
        <Card>
            <CardBody>
                <p>当前总金额{allMoney}$</p>
            </CardBody>
        </Card>
    );
}