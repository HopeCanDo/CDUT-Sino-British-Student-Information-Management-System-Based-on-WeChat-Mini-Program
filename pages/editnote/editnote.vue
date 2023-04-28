<template>
	<view>
		<view class="container">
			<textarea v-model="text" class="text"></textarea>
		</view>
		<view>
			<button type="primary" @tap="edit()">edit note</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				text: '',
				id: ''
			}
		},
		onLoad(event) {
			if(!uni.getStorageSync('user_name')){
				uni.showToast({
					title:'Please login!',
					icon:'error'
				})
				uni.navigateTo({
					url:'/pages/login/login'
				})
			}
			console.log('id=' + event.note_id);
			this.id = event.note_id;
			this.getnoteById();

		},
		methods: {
			getnoteById() {
				uniCloud.callFunction({
					name: 'getnoteById',
					data: {
						note_id: this.id
					},
					success: (res) => {
						console.log('--' + JSON.stringify(res));
						this.text = res.result.data[0].content;
					}
				})
			},
			edit() {
				uniCloud.callFunction({
					name: 'editnote',
					data: {
						note_content: this.text,
						note_id: this.id
					},
					success: (res) => {
						console.log('--'+JSON.stringify(res));
						uni.showToast({
							title:"Edit successfully!"
						})
						uni.switchTab({
							url:'/pages/note/note'
						})
					}
				})
			}
		}
	}
</script>

<style>
	.container {
		padding: 30rpx;
	}

	.text {
		background-color: #d0d0d0;
		width: 100%;
		min-height: 500rpx;
	}
</style>