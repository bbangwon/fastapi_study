<script>    
    import fastapi from "../lib/api";
    import Error from "../components/Error.svelte";
    import { push } from "svelte-spa-router";
    import moment from "moment/min/moment-with-locales";
    moment.locale('ko');
    
    export let params = {};
    let question_id = params.question_id;
    
    let question = {answers: []};
    let content = "";
    let error = {detail:[]};

    async function get_question() {
        question = await fastapi('get', '/api/question/detail/' + question_id)
        console.log(question);
    }

    get_question();

    async function post_answer(event) {
        event.preventDefault();
        let url = "/api/answer/create/" + question_id;
        let params = {
            content: content
        }
        try {
            const result = await fastapi('post', url, params);
            error = {detail:[]}
        } catch (e) {
            if(e.error)
                error = e.error;
            else
                alert(e);
        }        
        content = "";
        get_question();

    }
</script>

<div class="container my-3">
    <!-- 질문 -->
     <h2 class="border-bottom-py-2">{question.subject}</h2>
     <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{question.content}</div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}
                </div>
            </div>                
        </div>
     </div>
     <button class="btn btn-secondary" on:click={() => push('/')}>목록으로</button>
    <!-- 답변 -->
     <h5 class="border-bottom-my-3 py-2">{question.answers.length}개의 답변이 있습니다.</h5>
     {#each question.answers as answer}
     <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{answer.content}</div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {moment(answer.create_date).format("YYYY년 MM월 DD일 hh:mm a")}
                </div>
            </div>                
        </div>
     </div>
     {/each}
     <!-- 답변 등록 -->
     <Error error={error} />
     <form method="post" class="my-3">
        <div class="mb-3">
            <textarea row="10" bind:value={content} class="form-control"></textarea>            
        </div>
        <input type="submit" value="답변 등록" class="btn btn-primary" on:click={post_answer}>
     </form>
</div>