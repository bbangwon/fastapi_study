<script>    
    import fastapi from "../lib/api";
    import Error from "../components/Error.svelte";
    
    export let params = {};
    let question_id = params.question_id;
    
    let question = {answer: []};
    let content = "";
    let error = {detail:[]}

    async function get_question() {
        question = await fastapi('get', '/api/question/detail/' + question_id)
    }

    get_question();

    async function post_answer(event) {
        event.preventDefault();
        let url = "/api/answer/create/" + question_id;
        let params = {
            content: content
        }
        try {
            result = await fastapi('post', url, params);
            error = {detail:[]}
        } catch (e) {
            if(e.error)
                error = e.error;
            else
                alert(e.statusText);
        }        
        content = "";
        get_question();

    }
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>
<ul>
    {#each question.answers as answer}
        <li>{answer.content}</li>
    {/each}
</ul>
<Error error={error} />
<form method="post">
    <textarea rows="15" bind:value={content}></textarea>
    <input type="submit" value="답변등록" on:click="{post_answer}">
</form>

<style>
    textarea {
        width:100%;
    }
    input[type=submit] {
        margin-top:10px;
    }    
</style>