<template>
	<div id="app">
		<div class="bitcoin">
			<i class="fa-brands fa-bitcoin"></i> {{ record.data[0].amount }} / <i class="fa-solid fa-yen-sign"></i> {{ record.data[1].jpy }}<p><code class="bitcoin">{{ address }}</code></p>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data () {
		return {
			address: "3BqHXxraZyBapyNpJmniJDh9zqzuB8aoRr",
			record: null,
		}
	},
	mounted () {
			axios
				.get("https://aisyui.github.io/coin/btc.json")
				.then(response => (this.record = response));
	}
}
</script>
