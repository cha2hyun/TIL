import React from 'react';
import Styled from 'styled-components/native'

const Container = Styled.TouchableOpacity``;
const Icon = Styled.Image`
    height: 30px;
    width: 30px;
`;

interface Props {
    iconName: 'plus' | 'minus';
    onPress?: () => void;
}

const Button = ({ iconName, onPress }: Props) => {
    return (
        <Container onPress={onPress}>
            <Icon
                source = {
                    iconName === 'plus'
                    ? require('~/Assets/Images/add.png')
                    : require('~/Assets/Images/remove.png')
                }
            ></Icon>
        </Container>
    );
};
export default Button;