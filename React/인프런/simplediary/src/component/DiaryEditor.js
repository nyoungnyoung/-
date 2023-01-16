import { useRef, useState } from "react";

const DiaryEditor = ()  => {

    // input에 들어갈 내용을 관리할 author라는 state와
    // 이 state의 상태변화를 시켜줄 함수 setAuthor
    // const [author, setAuthor] = useState("");
    // const [content, setContent] = useState("");
    
    // 동작이 비슷한 state끼리는 묶어줄 수 있음
    const [state, setState] = useState({
        author: "",
        content: "",
        emotion: 1,
    })

    const authorinput = useRef();
    const contentinput = useRef();
    
    // state까지는 합쳤는데, 이벤트 핸들러가 두개로 나눠져있으니까 이상하다! 하나로 합쳐보자!!
    const handleChangeState = (e) => {
        // console.log(e.target.name);
        // console.log(e.target.value);

        setState({
            ...state,
            [e.target.name]: e.target.value,
        })
    }

    const handleSubmit = () => {
        if(state.author.length < 1) {
            // alert("작성자는 최소 1글자 이상 입력해주세요")
            // focus -> useRef 기능 사용 : useRef로 생성한 object의 현재 가리키는 값을 current라는 프로퍼티로 접근할 수 있다.
            authorinput.current.focus()
            return
        }

        if(state.content.length < 5) {
            // alert("일기 본문은 최소 5글자 이상 입력해주세요")
            // focus
            contentinput.current.focus()
            return
        }
        console.log(state);
        alert("저장 성공");
    }

    return (
        <div className="DiaryEditor">
            <h2>오늘의 일기</h2>
            <div>
                <input
                    ref={authorinput}
                    name="author"
                    value={state.author}
                    // onChange={(e) => {
                    //     // console.log(e.target.value);
                    //     // console.log(state.content)
                    //     setState({
                    //         // 스프레드 연산자로 원래 state의 값 펼쳐주고 author만 변경해주는 방식(관리하는 state가 많아질수록 편하다!)
                    //         ...state,
                    //         author: e.target.value,
                    //         // content: state.content
                    //     });
                    // }}
                    onChange={handleChangeState}
                />
            </div>
            <div>
                <textarea name="content" cols="30" rows="10"
                    ref={contentinput}
                    value={state.content}
                    // onChange={(e) => {
                    //     // console.log(e.target.value);
                    //     // console.log(state.author)
                    //     setState({
                    //         ...state,
                    //         content : e.target.value,
                    //     });
                    // }}
                    onChange={handleChangeState}
                    />
            </div>
            <div>
                <span>오늘의 감정점수 : </span>
                <select name="emotion" value={state.emotion} onChange={handleChangeState}>
                    <option value={1}>1</option>
                    <option value={2}>2</option>
                    <option value={3}>3</option>
                    <option value={4}>4</option>
                    <option value={5}>5</option>
                </select>
            </div>
            <div>
                <button onClick={handleSubmit}>일기 저장하기</button>
            </div>
        </div>
    )
};

export default DiaryEditor;