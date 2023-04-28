<template>
	<view>
		<text class="title">Add Schedule</text>
		<view class="container">
			Subject(abbreviation):
			<input v-model="text" class="input" maxlength="12">
			Techer:
			<input v-model="text1" class="input" maxlength="6">
			Classroom:
			<input v-model="text2" class="input" maxlength="5">
			Days of the week:
			<picker v-model="text3" @change="bindPickerChange" :range="array">
				<label>{{array[index]}}</label>
				<image class="dropdown-icon" src="/static/dropdown.png" mode="widthFix"></image>
			</picker>
			Time Period:
			<picker v-model="text4" @change="bindPickerChange1" :range="array2">
				<label>{{array2[index1]}}</label>
				<image class="dropdown-icon" src="/static/dropdown.png" mode="widthFix"></image>
			</picker>
		</view>
		<view>
			<button type="primary" @tap="edit()">edit schedule</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				text: '',
				text1: '',
				text2: '',
				text3: '',
				text4: '',
				array: ['--Please select--','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
				array2: ['--Please select--','8:10-8:55', '9:00-9:45', '8:10-9:45', '10:15-11:00', '11:05-11:50', '10:15-11:50', '14:30-15:15',
					'15:20-16:05', '14:30-16:05', '16:25-17:10', '17:15-18:00', '16:25-18:00'
				],
				index: 0,
				index1: 0,
				id: ''
			};
		},
		onLoad(event) {
			if (!uni.getStorageSync('user_name')) {
				uni.showToast({
					title: 'Please login!',
					icon: 'error'
				})
				uni.navigateTo({
					url: '/pages/login/login'
				})
			}
			console.log('id=' + event.schedule_id);
			this.id = event.schedule_id;
			this.getscheduleById();
		},
		methods: {
			getscheduleById() {
				uniCloud.callFunction({
					name: 'getscheduleById',
					data: {
						schedule_id: this.id
					},
					success: (res) => {
						console.log('--' + JSON.stringify(res));
						this.text = res.result.data[0].subject;
						this.text1 = res.result.data[0].teacher;
						this.text2 = res.result.data[0].classroom;
						this.text3 = res.result.data[0].day;
						this.text4 = res.result.data[0].time;
					}
				})
			},
			edit() {
				if (uni.getStorageSync('user_name') && this.text3 == 'Monday') {
					uniCloud.callFunction({
						name: 'editschdule',
						data: {
							subject: this.text,
							teacher: this.text1,
							day: this.text3,
							time: this.text4,
							classroom: this.text2,
							Monday: true,
							Tuesday: false,
							Wednesday: false,
							Thursday: false,
							Friday: false
						},
						success: (res) => {
							console.log('--' + JSON.stringify(res));
							uni.showToast({
								title: "Edit successfully!"
							})
							uni.redirectTo({
								url: '/pages/schedule/schedule'
							})
						}
					})
				} else if (uni.getStorageSync('user_name') && this.text3 == 'Tuesday') {
					uniCloud.callFunction({
						name: 'editschdule',
						data: {
							subject: this.text,
							teacher: this.text1,
							day: this.text3,
							time: this.text4,
							classroom: this.text2,
							Monday: false,
							Tuesday: true,
							Wednesday: false,
							Thursday: false,
							Friday: false
						},
						success: (res) => {
							console.log('--' + JSON.stringify(res));
							uni.showToast({
								title: "Edit successfully!"
							})
							uni.redirectTo({
								url: '/pages/schedule/schedule'
							})
						}
					})
				}
				else if (uni.getStorageSync('user_name') && this.text3 == 'Wednesday') {
					uniCloud.callFunction({
						name: 'editschdule',
						data: {
							subject: this.text,
							teacher: this.text1,
							day: this.text3,
							time: this.text4,
							classroom: this.text2,
							Monday: false,
							Tuesday: false,
							Wednesday: true,
							Thursday: false,
							Friday: false
						},
						success: (res) => {
							console.log('--' + JSON.stringify(res));
							uni.showToast({
								title: "Edit successfully!"
							})
							uni.redirectTo({
								url: '/pages/schedule/schedule'
							})
						}
					})
				}else if (uni.getStorageSync('user_name') && this.text3 == 'Thursday') {
					uniCloud.callFunction({
						name: 'editschdule',
						data: {
							subject: this.text,
							teacher: this.text1,
							day: this.text3,
							time: this.text4,
							classroom: this.text2,
							Monday: false,
							Tuesday: false,
							Wednesday: false,
							Thursday: true,
							Friday: false
						},
						success: (res) => {
							console.log('--' + JSON.stringify(res));
							uni.showToast({
								title: "Edit successfully!"
							})
							uni.redirectTo({
								url: '/pages/schedule/schedule'
							})
						}
					})
				}else if (uni.getStorageSync('user_name') && this.text3 == 'Friday') {
					uniCloud.callFunction({
						name: 'editschdule',
						data: {
							subject: this.text,
							teacher: this.text1,
							day: this.text3,
							time: this.text4,
							classroom: this.text2,
							Monday: false,
							Tuesday: false,
							Wednesday: false,
							Thursday: false,
							Friday: true
						},
						success: (res) => {
							console.log('--' + JSON.stringify(res));
							uni.showToast({
								title: "Edit successfully!"
							})
							uni.redirectTo({
								url: '/pages/schedule/schedule'
							})
						}
					})
				}

			},
			bindPickerChange: function(e) {
				this.index = e.target.value
				this.text3 = this.array[this.index]
			},
			bindPickerChange1: function(e) {
				this.index1 = e.target.value
				this.text4 = this.array2[this.index1]
			}
		}
	}
</script>

<style lang="scss">
	.container {
		padding: 30rpx;
	}

	.input {
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

	picker {
		border: solid 1rpx gray;
	}

	.dropdown-icon {
		height: 70rpx;
		width: 70rpx;
		position: absolute;
		right: 2%;
	}
</style>