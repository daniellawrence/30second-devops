# Create a basic helloworld.txt file
file "/tmp/helloworld.txt" do
  owner "root"
  group "root"
  mode 00544
  action :create
  content "Hello, World!"
end

# Install http://www.gnu.org/software/hello/
package "hello" do
  action :"install"
end
