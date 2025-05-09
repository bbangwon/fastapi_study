<script>
  let question_list = [];

  async function get_question_list() {
    const response = await fetch('http://127.0.0.1:8000/api/question/list')
    if (response.ok) {
      const data = await response.json();
      question_list = data;
    } else {
      console.error('Failed to fetch question list');
    }      
  }

  get_question_list();

</script>

<ul>
  {#each question_list as question}
    <li>{question.subject}</li>
  {/each}
</ul>