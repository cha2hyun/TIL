import React, {useState} from 'react';
import { PanResponder, ProgressViewIOSComponent } from 'react-native';
import Styled from 'styled-components/native';
import Button from '~/Components/Buttons';

const Container = Styled.SafeAreaView`
    flex: 1;
`;

const TitleContainer = Styled.View`
    flex: 1;
    justify-content: center;
    align-items: center;
`;

const TitleLabel = Styled.Text`
    font-size: 24px;
`;

const CountConatiner = Styled.View`
    flex: 2;
    justify-content: center;
    align-items: center;
`;

const CountLabel = Styled.Text`
    font-size: 24px;
    font-weight: bold;
`;

const ButtonContainer = Styled.View`
    flex: 1;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
`;

interface Props {
    title?: string;
    initValue: number;
}

interface State {
    count: number;
}

class Counter extends React.Component<Props, State> {
    constructor(props: Props) {
        super(props);
        console.log('constructor!')

        this.state = {
            count: props.initValue,
        };
    }

    render() {
        const { title } = this.props;
        const { count } = this.state;
        return(
            <Container>
                    { title && (
                    <TitleContainer>
                        <TitleLabel>{title}</TitleLabel>
                    </TitleContainer>
                )}
                <CountConatiner>
                    <CountLabel>{count}</CountLabel>                
                </CountConatiner>
                <ButtonContainer>
                    <Button iconName="plus" onPress={() => this.setState({ count: count + 1 })} />
                    <Button iconName="minus" onPress={() => this.setState({ count: count - 1 })} />
                </ButtonContainer>
            </Container>
        );
    }
}
// const Counter = ({ title, initValue}: Props) => {
//     const [count, setCount] = useState<number>(0);

//     return (
//         <Container>
//             { title && (
//                 <TitleContainer>
//                     <TitleLabel>{title}</TitleLabel>
//                 </TitleContainer>
//             )}
//             <CountConatiner>
//                 <CountLabel>{initValue + count}</CountLabel>                
//             </CountConatiner>
//             <ButtonContainer>
//                 <Button iconName="plus" onPress={() => setCount(count + 1)} />
//                 <Button iconName="minus" onPress={() => setCount(count - 1)} />
//             </ButtonContainer>
//         </Container>
//     );
// };

export default Counter;