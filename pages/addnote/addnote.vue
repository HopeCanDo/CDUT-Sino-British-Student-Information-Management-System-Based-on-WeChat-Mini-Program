<template>
	<view>
		<view class="container">
			<textarea v-model="text" class="text"></textarea>
		</view>
		<view>
			<button type="primary" @tap="save()">store note</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				text: ''
			};
		},
		onLoad() {
			if (!uni.getStorageSync('user_name')) {
				uni.showToast({
					title: 'Please login!',
					icon: 'error'
				})
				uni.navigateTo({
					url: '/pages/login/login'
				})
			}
		},
		methods: {
			getDate() {
				var nowdate = new Date();
				var year = nowdate.getFullYear(),
					month = nowdate.getMonth() + 1,
					date = nowdate.getDate(),
					time = nowdate.toLocaleTimeString();
				return year + '-' + month + '-' + date + "-" + time;
			},
			save() {
				if (uni.getStorageSync('use_name')) {
					uniCloud.callFunction({
						name: 'storenote',
						data: {
							content: this.text,
							user_name: uni.getStorageSync('user_name'),
							createdtime: this.getDate()
						},
						success: (res) => {
							console.log('==' + JSON.stringify(res))
							uni.showToast({
								title: 'Save successfully!',
								icon: 'none',
								position: 'bottom'
							});
							return;
						}
					})
					uni.redirectTo({
						url: "../note/note"
					})
				}else{
					uni.showToast({
						title:'Please login!',
						icon:'error'
					})
				}
			}

		}
	}
</script>

<style lang="scss">
	.container {
		padding: 30rpx;
	}

	.text {
		background-color: #d0d0d0;
		width: 100%;
		min-height: 500rpx;
	}
</style>