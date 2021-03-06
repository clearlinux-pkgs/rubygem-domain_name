#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-domain_name
Version  : 0.5.20160826
Release  : 11
URL      : https://rubygems.org/downloads/domain_name-0.5.20160826.gem
Source0  : https://rubygems.org/downloads/domain_name-0.5.20160826.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1 MPL-1.1
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rubygems-tasks
BuildRequires : rubygem-shoulda
BuildRequires : rubygem-test-unit

%description
domain_name
===========
Synopsis
--------
Domain Name manipulation library for Ruby

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n domain_name-0.5.20160826
gem spec %{SOURCE0} -l --ruby > rubygem-domain_name.gemspec

%build
export LANG=C
gem build rubygem-domain_name.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
domain_name-0.5.20160826.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/domain_name-0.5.20160826.gem
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/.document
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/README.md
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/data/public_suffix_list.dat
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/domain_name.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/lib/domain_name.rb
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/lib/domain_name/etld_data.rb
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/lib/domain_name/etld_data.rb.erb
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/lib/domain_name/punycode.rb
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/lib/domain_name/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/test/test_domain_name-punycode.rb
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/test/test_domain_name.rb
/usr/lib64/ruby/gems/2.3.0/gems/domain_name-0.5.20160826/tool/gen_etld_data.rb
/usr/lib64/ruby/gems/2.3.0/specifications/domain_name-0.5.20160826.gemspec
