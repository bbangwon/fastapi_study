<script>
    import { push } from "svelte-spa-router";
    import Error from "../components/Error.svelte";
    import fastapi from "../lib/api";

    let error = {detail:[]};
    let subject = '';
    let content = '';

    async function post_question(event) {
        event.preventDefault();
        let url = '/api/question/create';
        let params = {
            subject: subject,
            content: content
        };
        try {
            const result = await fastapi('post', url, params);
            error = {detail:[]};
            push('/');
        } catch (e) {
            if(e.error)
                error = e.error;
            else
                alert(e);
        }    
    }
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>
    <Error error={error} />
    <form method="post" class=my-3>
        <div class="mb-3">
            <label for="subjecct">제목</label>
            <input type="text" class="form-control" bind:value="{subject}">
        </div>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea class="form-control" rows="10" bind:value="{content}"></textarea>
        </div>
        <button class="btn btn-primary" type="submit" on:click={post_question}>저장하기</button>
    </form>
</div>