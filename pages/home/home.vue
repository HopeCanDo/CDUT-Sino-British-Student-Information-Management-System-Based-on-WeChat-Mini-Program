<template>
	<view class="content">
		<view id="box">
			<!-- <image class="bg-image" mode="scaleToFill" src="/static/bg.jpg"></image> -->
			<swiper indicator-color="white" autoplay interval="2000" circular>
				<swiper-item>
					<image src="/static/swiper/icon.png"></image>
				</swiper-item>
			</swiper>
		</view>
		<view class="title">Today's Schedule</view>
		<view @tap="schedule()">
			<image src="/static/schedule.jpg"></image>
		</view>
		<view class="title">Tool</view>
		<view class="top">
			<navigator url="/pages/grades/grades" class="ability">
				<text>GRADES</text>
				<image src="/static/grade.png" />
			</navigator>
			<navigator url="/pages/map/map" class="ability">
				<text>MAP</text>
				<image src="/static/wan_map.png" />
			</navigator>
		</view>
		<view class="top2">
			<navigator url="/pages/translates/translate" class="ability">
				<text>TRANSLATE</text>
				<image src="/static/translate.png" />
			</navigator>
			<navigator url="/pages/about/about" class="ability">
				<text>ABOUT</text>
				<image src="/static/about.png" />
			</navigator>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			};
		},
		// onLaunch() {
		// 	uni.clearStorageSync('user_name')
		// },
		onLoad() {
			uni.clearStorageSync('user_name')
		},
		onShow() {
			console.log(uni.getStorageSync('user_name'))
		},
		methods:{
			schedule(){
				uni.navigateTo({
					url:'/pages/schedule/schedule'
				})
			}
		}
	}
</script>

<style lang="scss">
	@keyframes animated-border {
		0% {
			box-shadow: 0 0 0 0 rgba(83, 232, 255, 0.4);
		}

		100% {
			box-shadow: 0 0 0 40rpx rgba(121, 255, 37, 0.0);
		}
	}

	#box {
		animation: animated-border 1.5s infinite;
	}

	.content {
		box-sizing: border-box;
		height: 100%;
		width: 100%;
		font-size: 28rpx;
		background-image: linear-gradient(208deg, #f3f3dc 10%, #cacaff 20%, #f8f6df 50%);
	}

	.top {
		display: flex;
		// justify-content: space-between;
		margin-top: 10rpx;

		.ability {
			margin-left: 8rpx;
			margin-right: 10rpx;
			width: 50%;
			color: #060219;
			height: 240rpx;
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: space-around;
			border-radius: 28rpx;
			font-size: 28rpx;
			font-weight: bolder;
			box-shadow: 9rpx 9rpx 10rpx #818181;

			&:nth-child(1) {
				background-image: linear-gradient(0deg, #ff6179 10%, #f8f8f8 100%);
			}

			&:nth-child(2) {
				background-image: linear-gradient(0deg, #ff743d 10%, #f8f8f8 100%);
			}

			image {
				height: 158rpx;
				width: 158rpx;
			}

			text {
				margin-top: 30rpx;
			}
		}
	}

	.top2 {
		display: flex;
		// justify-content: space-between;
		margin-top: 10rpx;

		.ability {
			margin-left: 8rpx;
			margin-right: 10rpx;
			width: 50%;
			color: #060219;
			height: 240rpx;
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: space-around;
			border-radius: 28rpx;
			font-size: 28rpx;
			font-weight: bolder;
			box-shadow: 9rpx 9rpx 10rpx #818181;

			&:nth-child(1) {
				background-image: linear-gradient(0deg, #ffd84b 10%, #f8f8f8 100%);
			}

			&:nth-child(2) {
				background-image: linear-gradient(0deg, #40ff99 10%, #f8f8f8 100%);
			}

			image {
				height: 158rpx;
				width: 158rpx;
			}

			text {
				margin-top: 30rpx;
			}
		}
	}

	swiper {
		height: 300rpx;
	}

	swiper image {
		width: 100%;
		height: 100%;
	}

	.bg-image {
		width: 100%;
		height: 100%;
		position: fixed;
		z-index: -1;
	}

	.title {
		padding: 50rpx 35rpx 38rpx 35rpx;
		font-size: 32rpx;
		font-weight: bolder;
		color: black;
		position: relative;

		&::after {
			content: '';
			position: absolute;
			left: 13rpx;
			background-color: #2eeaf4;
			width: 12rpx;
			height: 33%;
			bottom: 37rpx;
			border-radius: 10rpx;
		}
	}

	image {
		height: 300rpx;
		padding-top: 10rpx;
		width: 100%;

	}

	.center_top {
		padding: 2rpx 10rpx;

		text {
			margin: 0 28rpx;
			font-family: Arial;

			&:last-child {
				position: absolute;
				right: 18rpx;
			}
		}
	}
</style>