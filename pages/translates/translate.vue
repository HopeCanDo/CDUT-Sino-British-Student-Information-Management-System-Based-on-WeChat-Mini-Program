<template>
	<view class="wrapper">
		<view class="content">
			<image class="bg-set" src="/static/background3.jpg"></image>
			<view class="form-item">
				<view class="title">Translation content:</view>
				<view>
					<textarea :value="params.sourceText" :disabled="status" maxlength="110" @input="textChange"
						placeholder="Search something else.."
						style="border: 1px solid #c0c0c0; padding: 10px;background-color: white;width: 92%;height: 350rpx;border-radius: 28rpx;" />
				</view>
			</view>
			<view class="form-item2">
				<view class="title">Target Language:</view>
				<picker class="picker" @change="translateChange" :value="index" :range="translateOption"
					range-key="text">
					<view class="uni-input">{{ translateOption[index].text }}</view>
				</picker>
			</view>
			<view>
				<button type="primary" @click="startTranslate" v-bind:disabled="status"
					style="border-radius: 28rpx;">{{ status ? 'Translating..' : 'TRANSLATE' }}</button>
			</view>
			<view class="form-item">
				<view class="title">Translation results:</view>
				<view style="background-color: white;height: 500rpx;border-radius: 28rpx;padding: 10rpx;">
					{{ translateResult }}</view>
			</view>
		</view>
	</view>
</template>


<script>
	import {
		translateOption
	} from './dictionary.js';
	import {
		getTextTranslateResult
	} from '@/js_sdk/tencentcloud-plugin-tmt';
	export default {
		data() {
			return {
				status: false, // Whether to start translation
				index: 0, // Selected language conversion option subscript
				translateType: 'zh-en',
				translateOption,
				params: {
					sourceText: '', // Composite Text
					source: 'zh', // source language
					target: 'en' // target language
				},
				translateResult: '',
				text1: 'Hello, welcome to the Hope project!'
			};
		},
		methods: {
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
				this.params.sourceText = this.text1;
			},
			translateChange(e) {
				this.index = e.target.value;
				const arr = this.translateOption[this.index].value.split('-');
				[this.params.source, this.params.target] = arr;
			},
			textChange(e) {
				this.params.sourceText = e.target.value;
			},
			async startTranslate() {
				try {
					this.status = true;
					this.translateResult = '';
					uni.showLoading({
						mask: true
					});
					const paramsData = {
						sourceText: this.params.sourceText,
						source: this.params.source,
						target: this.params.target
					};
					const result = await getTextTranslateResult(paramsData);
					this.translateResult = result.TargetText;
					uni.hideLoading();
				} catch (error) {
					uni.showToast({
						icon: 'none',
						title: error.message
					});
				} finally {
					this.status = false;
				}
			}
		}
	};
</script>

<style lang="scss">
	page {
		background-image: linear-gradient(208deg, #f3f3dc 10%, #cacaff 20%, #f8f6df 50%);
	}

	.wrapper {
		margin: 20rpx auto;
	}

	.content {
		margin: 20rpx 40rpx;
	}

	.content .title {
		margin-bottom: 8rpx;
		padding: 10rpx 35rpx 10rpx 35rpx;
		font-size: 30rpx;
		font-weight: bolder;
		color: black;
		position: relative;

		&::after {
			content: '';
			position: absolute;
			left: 13rpx;
			background-color: #2eeaf4;
			width: 12rpx;
			height: 66%;
			bottom: 10rpx;
			border-radius: 10rpx;
		}
	}

	.content .form-item {
		margin-bottom: 20rpx;
	}

	.content .form-item2 {
		display: flex;
	}

	.content .form-item .radio {
		margin-right: 10px;
	}

	.content .form-item input {
		border: 1px solid #c0c0c0;
		padding: 10px;
	}

	.content button {
		margin: 40rpx 0;
		background-color: blue;
	}

	.bg-set {
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		z-index: -1;
	}

	.picker {
		background-color: white;
		font-size: 30rpx;
		font-weight: bolder;
		border-radius: 16rpx;
		padding: 12rpx 4rpx 0rpx 4rpx;
	}
</style>