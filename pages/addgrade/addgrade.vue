<template>
	<view>
		<text class="title">Add Grade</text>
		<view class="container">
			Subject:
			<input v-model="text" class="input">
			Level:
			<input v-model="text1" class="input">
			Score:
			<input v-model="text2" class="input">
		</view>
		<view>
			<button type="primary" @tap="save()">store grade</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				text: '',
				text1: '',
				text2: ''
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
				if (uni.getStorageSync('user_name')) {
					uniCloud.callFunction({
						name: 'addgrade',
						data: {
							content: this.text,
							user_name: uni.getStorageSync('user_name'),
							createdtime: this.getDate(),
							level:this.text1,
							score:this.text2
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
						url: "../grades/grades"
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
	.input{
		border: solid 1rpx gray;
	}
	.title {
		text-align: center;
		display: block;
		padding: 50rpx 35rpx 38rpx 35rpx;
		font-size: 32rpx;
		font-weight: bolder;
		color: black;
	}
</style>