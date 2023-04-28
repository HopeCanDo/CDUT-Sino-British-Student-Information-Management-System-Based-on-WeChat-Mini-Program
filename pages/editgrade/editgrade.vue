<template>
	<view>
		<text class="title">Add Grade</text>
		<view class="container">
			Subject:
			<input v-model="text" class="input" :id="text"/>
			Level:
			<input v-model="text1" class="input"/>
			Score:
			<input v-model="text2" class="input"/>
		</view>
		<view>
			<button type="primary" @tap="edit()">edit grade</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				text: '',
				text1:'',
				text2:'',
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
			console.log('id=' + event.grade_id);
			this.id = event.grade_id;
			this.getgradeById();
		},
		methods: {
			getgradeById() {
				uniCloud.callFunction({
					name: 'getgradeById',
					data: {
						grade_id: this.id
					},
					success: (res) => {
						console.log('--' + JSON.stringify(res));
						this.text = res.result.data[0].content;
					}
				})
			},
			edit() {
				uniCloud.callFunction({
					name: 'editgrade',
					data: {
						grade_content: this.text,
						grade_level:this.text1,
						grade_score:this.text2,
						grade_id: this.id
					},
					success: (res) => {
						console.log('--'+JSON.stringify(res));
						uni.showToast({
							title:"Edit successfully!"
						})
						uni.redirectTo({
							url:'/pages/grades/grades'
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
	.title {
		text-align: center;
		display: block;
		padding: 50rpx 35rpx 38rpx 35rpx;
		font-size: 32rpx;
		font-weight: bolder;
		color: black;
	}
	.input{
		border: solid 1rpx gray;
	}
</style>