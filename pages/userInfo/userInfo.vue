<template>
	<view class="container">
		<view class="profile">
			<image class="avatar" src="../../static/tab/user.png" @tap="act()"></image>
			<view class="name" v-model="user_name">{{user_name}}</view>
			<image class="shui" src="../../static/shui.gif"></image>
		</view>
		<view class="menu">
			<button @tap="personel()">
				<view class="menu-item">
					<image class="icon" src="../../static/personal_info.png"> </image>
					<text class="text">Personal information</text>
				</view>
			</button>
			<button @tap="github()">
				<view class="menu-item">
					<image class="icon" src="../../static/github.png"> </image>
					<text class="text">Github</text>
				</view>
			</button>
			<button @tap="about()">
				<view class="menu-item">
					<image class="icon" src="../../static/about.png"> </image>
					<text class="text">About Us</text>
				</view>
			</button>
			<button data-name="shareBtn" open-type="share">
				<view class="menu-item">
					<image class="icon" src="../../static/share.png"> </image>
					<text class="text">Share Applet</text>
				</view>
			</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				user_name: ""
			}
		},
		onLoad: function(option) {
			if (!uni.getStorageSync('user_name')) {
				uni.showToast({
					title: 'Please login!',
					icon: 'error'
				})
				uni.navigateTo({
					url: '/pages/login/login'
				})
			}
			this.user_name = uni.getStorageSync('user_name')
		},
		onShow: function(event) {
			this.user_name = uni.getStorageSync('user_name')
		},
		onShareAppMessage: function(res) {
			return {
				title: 'CDUT sino-british',
				path: 'pages/home/home'
			}

		},
		methods: {
			github() {
				uni.showModal({
					title: 'Project Github Address',
					content: 'https://github.com/HopecanDo/CDUT-Sino-British-Student-Information-Management-System-Based-on-WeChat-Mini-Program/'
				})
			},
			personel() {
				uni.navigateTo({
					url: '/pages/personal/personal'
				})
			},
			about() {
				uni.navigateTo({
					url: '/pages/about/about'
				})
			},
			act() {
				if (!uni.getStorageSync('user_name')) {
					uni.navigateTo({
						url: '/pages/login/login'
					})
					console.log('login');
				} else {
					uni.showModal({
						title: 'hint',
						content: 'Are you sure to log out?',
						success: function(res) {
							if (res.confirm) {
								uni.clearStorageSync('user_name')
								uni.showToast({
									title: 'Log out!'
								})
								uni.reLaunch({
									url: '/pages/home/home'
								})
							}
						}

					})
				}
			}
		}
	}
</script>


<style lang="scss">
	page {
		background-image: linear-gradient(208deg, #f3f3dc 10%, #cacaff 20%, #f8f6df 50%);
	}

	.container {

		height: 100%;
		width: 100%;
	}

	.profile {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 10px;
		justify-content: center;
	}

	.avatar {
		width: 80px;
		height: 80px;
		border-radius: 50%;
	}

	.name {
		margin-top: 5px;
		font-size: 20px;
	}

	.shui {
		width: 100%;
		mix-blend-mode: screen;
		height: 25px;
	}

	.menu {

		height: 100%;
		background-color: white;
	}

	.menu-item {
		display: flex;
		align-items: center;
		padding: 5px;
		// 	border-bottom: 1rpx solid gray;

	}

	.icon {
		width: 20px;
		height: 20px;
		margin-bottom: 10px;
	}

	.text {
		font-size: 12px;
	}

	button {
		width: 100%;
		background-color: white;
	}
</style>