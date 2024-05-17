#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/proc_fs.h>
#include <linux/jiffies.h>
#include <linux/sched.h>
#include <linux/uaccess.h>
#include <linux/seq_file.h>
#include <linux/fs.h>

#define MODULE_VERS "1.0"
#define MODULE_NAME "procfs_example"
#define FOOBAR_LEN 8

struct fb_data_t {
    char name[FOOBAR_LEN + 1];
    char value[FOOBAR_LEN + 1];
};

static struct proc_dir_entry *example_dir, *foo_file, *bar_file, *jiffies_file, *symlink;
struct fb_data_t foo_data, bar_data;
int foo_len, foo_temp, bar_len, bar_temp;
int jiff_temp = -1;
char tempstr[FOOBAR_LEN * 2 + 5];

// jiffies文件操作函数
ssize_t read_jiffies_proc(struct file *filp, char __user *buf, size_t count, loff_t *offp) {
    char tempstring[100] = "";
    int bytes;
    if (jiff_temp != 0)
        jiff_temp = sprintf(tempstring, "jiffies=%ld\n", jiffies);
    if (count > jiff_temp)
        count = jiff_temp;
    jiff_temp = jiff_temp - count;
    bytes = copy_to_user(buf, tempstring, count) ? -EFAULT : count;
    if (bytes == 0)
        jiff_temp = -1;
    return bytes;
}

// proc_ops结构定义
static const struct proc_ops jiffies_proc_ops = {
    .proc_read = read_jiffies_proc,
};

// foo文件操作函数
ssize_t read_foo_proc(struct file *filp, char __user *buf, size_t count, loff_t *offp) {
    if (count > foo_temp)
        count = foo_temp;
    foo_temp = foo_temp - count;
    strcpy(tempstr, foo_data.name);
    strcat(tempstr, "='");
    strcat(tempstr, foo_data.value);
    strcat(tempstr, "'\n");
    if (copy_to_user(buf, tempstr, count))
        return -EFAULT;
    if (count == 0)
        foo_temp = foo_len + 4;
    return count;
}

ssize_t write_foo_proc(struct file *filp, const char __user *buf, size_t count, loff_t *offp) {
    int len = count > FOOBAR_LEN ? FOOBAR_LEN : count;
    if (copy_from_user(foo_data.value, buf, len))
        return -EFAULT;
    foo_data.value[len-1] = '\0';
    foo_len = strlen(foo_data.name) + strlen(foo_data.value);
    foo_temp = foo_len + 4;
    return len;
}

static const struct proc_ops foo_proc_ops = {
    .proc_read = read_foo_proc,
    .proc_write = write_foo_proc,
};

// bar文件操作函数
ssize_t read_bar_proc(struct file *filp, char __user *buf, size_t count, loff_t *offp) {
    if (count > bar_temp)
        count = bar_temp;
    bar_temp = bar_temp - count;
    strcpy(tempstr, bar_data.name);
    strcat(tempstr, "='");
    strcat(tempstr, bar_data.value);
    strcat(tempstr, "'\n");
    if (copy_to_user(buf, tempstr, count))
        return -EFAULT;
    if (count == 0)
        bar_temp = bar_len + 4;
    return count;
}

ssize_t write_bar_proc(struct file *filp, const char __user *buf, size_t count, loff_t *offp) {
    int len = count > FOOBAR_LEN ? FOOBAR_LEN : count;
    if (copy_from_user(bar_data.value, buf, len))
        return -EFAULT;
    bar_data.value[len-1] = '\0';
    bar_len = strlen(bar_data.name) + strlen(bar_data.value);
    bar_temp = bar_len + 4;
    return len;
}

static const struct proc_ops bar_proc_ops = {
    .proc_read = read_bar_proc,
    .proc_write = write_bar_proc,
};

// 模块init函数
static int __init init_procfs_example(void) {
    example_dir = proc_mkdir(MODULE_NAME, NULL);
    if (!example_dir)
        return -ENOMEM;

    jiffies_file = proc_create("jiffies", 0444, example_dir, &jiffies_proc_ops);
    if (!jiffies_file)
        goto out_jiffies;

    strcpy(foo_data.name, "foo");
    strcpy(foo_data.value, "foo");
    foo_len = strlen(foo_data.name) + strlen(foo_data.value);
    foo_temp = foo_len + 4;
    foo_file = proc_create("foo", 0444, example_dir, &foo_proc_ops);
    if (!foo_file)
        goto out_foo;

    strcpy(bar_data.name, "bar");
    strcpy(bar_data.value, "bar");
    bar_len = strlen(bar_data.name) + strlen(bar_data.value);
    bar_temp = bar_len + 4;
    bar_file = proc_create("bar", 0444, example_dir, &bar_proc_ops);
    if (!bar_file)
        goto out_bar;

    symlink = proc_symlink("jiffies_too", example_dir, "jiffies");
    if (!symlink)
        goto out_symlink;

    printk(KERN_INFO "%s%s initialised\n", MODULE_NAME, MODULE_VERS);
    return 0;

out_symlink:
    remove_proc_entry("bar", example_dir);
out_bar:
    remove_proc_entry("foo", example_dir);
out_foo:
    remove_proc_entry("jiffies", example_dir);
out_jiffies:
    remove_proc_entry(MODULE_NAME, NULL);
    return -ENOMEM;
}

// 模块cleanup函数
static void __exit cleanup_procfs_example(void) {
    remove_proc_entry("jiffies_too", example_dir);
    remove_proc_entry("bar", example_dir);
    remove_proc_entry("foo", example_dir);
    remove_proc_entry("jiffies", example_dir);
    remove_proc_entry(MODULE_NAME, NULL);
    printk(KERN_INFO "%s%s removed\n", MODULE_NAME, MODULE_VERS);
}

MODULE_LICENSE("GPL");
module_init(init_procfs_example);
module_exit(cleanup_procfs_example);
MODULE_DESCRIPTION("proc filesystem example");
