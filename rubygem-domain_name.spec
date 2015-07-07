Name     : rubygem-domain_name
Version  : 0.5.24
Release  : 4
URL      : https://rubygems.org/downloads/domain_name-0.5.24.gem
Source0  : https://rubygems.org/downloads/domain_name-0.5.24.gem
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
BuildRequires : rubygem-unf
BuildRequires : rubygem-unf_ext

%description
domain_name
===========
Synopsis
--------
Domain Name manipulation library for Ruby

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n domain_name-0.5.24
gem spec %{SOURCE0} -l --ruby > rubygem-domain_name.gemspec

%build
gem build rubygem-domain_name.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
domain_name-0.5.24.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/domain_name-0.5.24
sed -i.orig \
    -e '/begin/,/end/d' \
    -e '/bundler/d' \
    test/helper.rb
sed -i.minitest \
    -e 's|Test::Unit::TestCase|Minitest::Test|' \
    test/*.rb
    cat > test/unit.rb << EOF
    gem "minitest"
    require "minitest/autorun"
rake --trace test TESTOPTS="-v"
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/domain_name-0.5.24.gem
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/%3c%3d%3e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/%3c%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/%3c-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/%3e%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/%3e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/Punycode/ArgumentError/cdesc-ArgumentError.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/Punycode/BufferOverflowError/cdesc-BufferOverflowError.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/Punycode/cdesc-Punycode.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/Punycode/decode-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/Punycode/decode_hostname-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/Punycode/encode-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/Punycode/encode_hostname-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/canonical%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/canonical_tld%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/cdesc-DomainName.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/cookie_domain%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/domain-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/domain_idn-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/etld_data-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/hostname-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/hostname_idn-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/idn-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/ipaddr%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/ipaddr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/normalize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/superdomain-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/tld-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/tld_idn-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/to_str-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/DomainName/uri_host-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/Object/DomainName-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/page-LICENSE_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/domain_name-0.5.24/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/.document
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/README.md
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/data/effective_tld_names.dat
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/domain_name.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/lib/domain_name.rb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/lib/domain_name/etld_data.rb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/lib/domain_name/etld_data.rb.erb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/lib/domain_name/punycode.rb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/lib/domain_name/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/test/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/test/helper.rb.minitest
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/test/helper.rb.orig
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/test/test_domain_name-punycode.rb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/test/test_domain_name-punycode.rb.minitest
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/test/test_domain_name.rb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/test/test_domain_name.rb.minitest
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/test/unit.rb
/usr/lib64/ruby/gems/2.2.0/gems/domain_name-0.5.24/tool/gen_etld_data.rb
/usr/lib64/ruby/gems/2.2.0/specifications/domain_name-0.5.24.gemspec
